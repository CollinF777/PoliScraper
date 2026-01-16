import plotly.graph_objs as go
from plotly.subplots import make_subplots
import math

# This created hover text for whenever you go over a data point
def create_hover_text(result):
    hover_text = f"<b>{result['name']}</b><br>"
    hover_text += f"Rating: {result['bias_rating']}<br>"
    hover_text += f"Known Bias: {result['known_bias']}<br>"
    hover_text += f"Calculated Bias: {result['calculated_bias']}<br>"
    hover_text += f"Credibility: {result['reliability']}<br>"
    hover_text += f"Total Keywords: {result['total_keywords']}<br>"
    hover_text += f"Left: {result['scores']['left']}<br>"
    hover_text += f"Center: {result['scores']['center']}<br>"
    hover_text += f"Right: {result['scores']['right']}<br>"
    hover_text += f"Source: {result['source']}<br>"
    return hover_text

# Adjusts label positions to avoid overlaps and increase readability
def adjust_label_pos(results):
    positions = {}

    # Group by similar positions
    position_groups = []
    for result in results:
        pos = (result["known_bias"], result["reliability"])

        # Find if this position is close to an already existing group
        added = False
        for group in position_groups:
            if any(abs(pos[0] -p[0]) < p[0] and abs(pos[1] - p[1]) < 1.0 for p in [r["pos"] for r in group]):
                group.append({"result": result, "pos": pos})
                added = True
                break

            if not added:
                position_groups.append([{"result": result, "pos": pos}])
    # Assign offsets to items in each group
    for group in position_groups:
        if len(group) == 1:
            # Single item, put label above
            result = group[0]["result"]
            positions[result["name"]] = (0, 0.6)
        else:
            # Multiple items, spread out labels
            for i, item in enumerate(group):
                result = item["result"]
                angle = (i/len(group)) * 2 * math.pi
                x_offset = 0.4 * math.cos(angle)
                y_offset = 0.6 + 0.3 * math.sin(angle)
                positions[result["name"]] = (x_offset, y_offset)

    return positions

# Define color mapping for bias values
def get_color(bias_value):
    if bias_value < -1.5:
        return 'rgb(66, 133, 244)'  # Blue for left
    elif bias_value > 1.5:
        return 'rgb(234, 67, 53)'   # Red for right
    else:
        return 'rgb(156, 39, 176)'  # Purple for center

"""
Creates interactive Plotly chart
This chart displays:
X-axis: Political bias (-5 left to +5 right)
Y-axis: Credibility score (0-10)
Circle markers: Known bias position from AllSides
Diamond markers: Calculated bias from keyword analysis
Connecting lines: Connecting known to calculated (shows difference)
"""
def create_bias_chart(results):
    fig = go.Figure()

    #  Sort results by known bias for better visual organization
    sorted_results = sorted(results, key=lambda x: x["known_bias"])

    # Calculate label positions to avoid overlap
    label_positions = adjust_label_pos(sorted_results)

    # Add connecting lines first (so they appear behind markers)
    for result in sorted_results:
        fig.add_trace(go.Scatter(
            x=[result["known_bias"], result["calculated_bias"]],
            y=[result["reliability"], result["reliability"]],
            mode="lines",
            line=dict(
                color="rgba(128, 128, 128, 0.25)",
                width=1.5,
            ),
            hoverinfo="skip",
            showlegend=False
        ))

    # Add known bias markers (circles)
    known_x = [r["known_bias"] for r in sorted_results]
    known_y = [r["reliability"] for r in sorted_results]
    known_colors = [get_color(r["known_bias"]) for r in sorted_results]
    known_sizes = [max(18, 15 + r["total_keywords"] / 10) for r in sorted_results]

    fig.add_trace(go.Scatter(
        x=known_x,  # Pos on bias scale
        y=known_y, # Pos on credibility scale
        mode="markers", # Display as marker
        marker=dict(
            size=known_sizes,
            color=known_colors,
            line=dict(width=2.5, color="white"),
            symbol="circle",
            opacity=0.85
        ),
        text=[r["name"] for r in sorted_results], # Makes label the website name
        hovertext=[create_hover_text(r) for r in sorted_results], # Add hover info
        hoverinfo="text",
        name="Known Bias",
        showlegend=True
    ))

    # Add calculated bias markers (diamonds)
    calc_x = [r["calculated_bias"] for r in sorted_results]
    calc_y = [r["reliability"] for r in sorted_results]
    calc_colors = [get_color(r["calculated_bias"]) for r in sorted_results]

    fig.add_trace(go.Scatter(
        x=calc_x,
        y=calc_y,
        mode="markers",
        marker=dict(
            size=14,
            color=calc_colors,
            line=dict(width=2.5, color="white"),
            symbol="diamond",
            opacity=0.85
        ),
        hovertext=[create_hover_text(r) for r in sorted_results],
        hoverinfo="text",
        name="Calculated Bias",
        showlegend=True
    ))

    # Add text labels with arrows to avoid overlap
    for result in sorted_results:
        x_offset, y_offset = label_positions[result["name"]]

        fig.add_annotation(
            x=result["known_bias"],
            y=result["reliability"],
            ax=result["known_bias"] + x_offset,
            ay=result["reliability"] + y_offset,
            text=result["name"],
            showarrow=True,
            arrowhead=2,
            arrowsize=0.8,
            arrowwidth=1,
            arrowcolor="rgba(100,100,100,0.4)",
            font=dict(size=9, color="rgba(0,0,0,0.85)", family="Arial"),
            bgcolor="rgba(255,255,255,0.9)",
            bordercolor="rgba(0,0,0,0.15)",
            borderwidth=1,
            borderpad=3,
            opacity=0.95
        )

    # Add vertical reference lines
    fig.add_vline(x=0, line_dash="dash", line_color="rgba(0,0,0,0.3)", line_width=1.5)

    # Add shaded background regions with labels
    fig.add_vrect(x0=-5, x1=-1.5, fillcolor="rgba(66, 133, 244, 0.06)",
                  layer="below", line_width=0)
    fig.add_vrect(x0=-1.5, x1=1.5, fillcolor="rgba(156, 39, 176, 0.06)",
                  layer="below", line_width=0)
    fig.add_vrect(x0=1.5, x1=5, fillcolor="rgba(234, 67, 53, 0.06)",
                  layer="below", line_width=0)

    # Add region labels
    fig.add_annotation(x=-3.25, y=10.2, text="LEFT", showarrow=False,
                       font=dict(size=11, color="rgba(66, 133, 244, 0.6)", family="Arial Black"))
    fig.add_annotation(x=0, y=10.2, text="CENTER", showarrow=False,
                       font=dict(size=11, color="rgba(156, 39, 176, 0.6)", family="Arial Black"))
    fig.add_annotation(x=3.25, y=10.2, text="RIGHT", showarrow=False,
                       font=dict(size=11, color="rgba(234, 67, 53, 0.6)", family="Arial Black"))

    # Configure layout
    fig.update_layout(
        title={
            "text": "Media Bias Analysis: Known vs. Calculated<br><sub>Data sources: AllSides Media Bias Ratings | Media Bias/Fact Check</sub>",
            "x": 0.5,
            "xanchor": "center",
            "font": {"size": 20, "color": "#2c3e50", "family": "Arial"}
        },
        xaxis=dict(
            title="Political Bias Score",
            range=[-5.5, 5.5],
            tickmode="linear",
            tick0=-5,
            dtick=1,
            showgrid=True,
            gridcolor="rgba(0,0,0,0.08)",
            zeroline=True,
            zerolinecolor="rgba(0,0,0,0.3)",
            zerolinewidth=2
        ),
        yaxis=dict(
            title="Credibility Score (0-10)",
            range=[-0.5, 11],
            tickmode="linear",
            tick0=0,
            dtick=1,
            showgrid=True,
            gridcolor="rgba(0,0,0,0.08)"
        ),
        plot_bgcolor="white",
        paper_bgcolor="#fafafa",
        height=800,
        width=1300,
        hovermode="closest",
        legend=dict(
            x=0.02,
            y=0.98,
            bgcolor="rgba(255,255,255,0.95)",
            bordercolor="rgba(0,0,0,0.2)",
            borderwidth=1.5,
            font=dict(size=11)
        ),
        margin=dict(l=80, r=80, t=120, b=80)
    )

    # Add explanatory annotation
    fig.add_annotation(
        text="<b>How to read this chart:</b><br>" +
             "○ Circles = Known bias (AllSides)<br>" +
             "◇ Diamonds = Calculated bias (keyword analysis)<br>" +
             "― Lines connect the two measurements<br>" +
             "Larger circles = More keywords found",
        xref="paper", yref="paper",
        x=0.02, y=0.02,
        showarrow=False,
        bgcolor="rgba(255,255,255,0.95)",
        bordercolor="rgba(0,0,0,0.2)",
        borderwidth=1.5,
        font=dict(size=10, family="Arial"),
        align="left",
        xanchor="left",
        yanchor="bottom"
    )

    return fig

# Display chart in browser
def display_chart(fig):
    fig.show()

def save_chart(fig, filename="political_bias_chart.html"):
    fig.write_html(filename)
    print(f"Chart saved at {filename}")