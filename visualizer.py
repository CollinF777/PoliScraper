import plotly.graph_objs as go

# This created hover text for whenever you go over a data point
def create_hover_text(result):
    hover_text = f"<b>{result["name"]}</b></br>"
    hover_text += f"Rating: {result["bias_rating"]}</br>"
    hover_text += f"Known Bias: {result["known_bias"]}</br>"
    hover_text += f"Calculated Bias: {result["calculated_bias"]}</br>"
    hover_text += f"Credibility: {result["reliability"]}</br>"
    hover_text += f"Total Keywords: {result["total_keywords"]}</br>"
    hover_text += f"Left: {result["scores"]["left"]}</br>"
    hover_text += f"Center: {result["scores"]["center"]}</br>"
    hover_text += f"Right: {result["scores"]["right"]}</br>"
    hover_text += f"Source: {result["source"]}</br>"
    return hover_text

"""
Creates interactive Plotly chart
This chart displays:
X-axis: Political bias (-5 left to +5 right)
Y-axis: Credibility score (0-10)
Circle markers: Known bias position from AllSides
Diamond markers: Calculated bias from keyword analysis
Dotted lines: Connecting known to calculated (shows difference)
Marker size: Based on total keyword count
Marker color: Gradient from blue (left) to red (right)
"""
def create_bias_chart(results):
    fig = go.Figure()

    # Add data points for each scraped website
    for result in results:
        bias_diff = abs(result["known_bias"] - result["calculated_bias"])

        # Add circle marker for known bias
        fig.add_trace(go.Scatter(
            x=[result["known_bias"]], # Pos on bias scale
            y=[result["reliability"]], # Pos on credibility scale
            mode="markers+text", # Show both marker and text label
            marker=dict(
                # Marker size increases with more keywords aka more data = bigger
                size=15 + result["total_keywords"] / 5,
                # Color based off calculated bias
                color=result["calculated_bias"],
                # Color scale is a reversed red-blue scale
                colorscale="RdBu_r",
                cmin=-5, # Min color scale
                cmax=5, # Max color scale
                line=dict(width=2, color="white"), # Adds white border around marker
                colorbar=dict(title="Calculated</br>Bias"), # Legend for color sclae
                symbol="circle", # Makes it a circle (duh)
            ),
            text=result["name"], # Makes label the website name
            textposition="top center", # Position label above the marker
            hovertext=create_hover_text(result), # Add hover info
            hoverinfo="text", # Only allow custom hover text
            name=result["name"], # Legend name (this wont be shown due to showLegend but can be changed)
            showlegend=False
        ))

        # Add dotted line connecting known and calculated bias
        fig.add_trace(go.Scatter(
            x=[result["known_bias"], result["calculated_bias"]], # Start and end points
            y=[result["reliability"], result["reliability"]], # Y stays the same
            mode="lines", # Only show the line, no need for markers
            line=dict(
                color="rgba(100, 100, 100, 0.4)",
                width=2,
                dash="dot" # Dotted line
            ),
            hoverinfo="skip", # No need for hover info on lines
            showlegend=False
        ))

        # Add diamond marker for calculated bias position
        fig.add_trace(go.Scatter(
            x=[result["calculated_bias"]], # Position from keyword analysis
            y=[result["reliability"]],
            mode="markers",
            marker=dict(
                size=10,
                color=result["calculated_bias"],
                colorscale="RdBu_r",
                cmin=-5,
                cmax=5,
                symbol="diamond",
                line=dict(width=2, color="white"),
            )
        ))

        # Adds vertical line at x=0 to display center
        fig.add_vline(x=0, line_dash="dash", line_color="gray", opacity=0.5)

        # Background rectangles that shades each region
        fig.add_vrect(x0=-5, x1=-1.5, fillcolor="blue", opacity=0.1, line_width=0)
        fig.add_vrect(x0=-1.5, x1=1.5, fillcolor="purple", opacity=0.1, line_width=0)
        fig.add_vrect(x0=1.5, x1=5, fillcolor="red", opacity=0.1, line_width=0)

        # Configure overall chart layout
        fig.update_layout(
            title="Political Bias Comparison: Known vs Calculated </br><sub>Known bias from Allsides Media Bias Ratings | Credibility from Media Bias/Fact Check</sub>",
            xaxis_title="Political Bias",
            yaxis_title="Credibility Score",
            xaxis=dict(range=[-5,5], zeroline=True),
            yaxis=dict(range=[0,10], zeroline=True),
            showlegend=False,
            height=600,
            width=900,
            hovermode="closest", # Show hover for nearest point
            annotations=[
                # Add text box explaining symbols
                dict(
                    text="Circle = Known Bias (AllSides)<br>Diamond = Calculated Bias from Keywords</br>Dotted Line = Difference",
                    xref="paper", yref="paper", # Position relative to plot area
                    x=0.02, y=-0.98, # Top left corner
                    showarrow=False,
                    bgcolor="rgba(255,255,255,0.8)",
                    bordercolor="gray",
                    borderwidth=1,
                    font=dict(size=10),
                    align="left",
                    xanchor="left",
                    yanchor="top",
                )
            ]
        )
        return fig

# Display chart in browser
def display_chart(fig):
    fig.show()

def save_chart(fig, filename="political_bias_chart.html"):
    fig.write_html(filename)
    print(f"Chart saved at {filename}")