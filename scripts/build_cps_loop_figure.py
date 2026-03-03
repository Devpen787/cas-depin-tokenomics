"""
build_cps_loop_figure.py
Generates Figure 1: Cyber-Physical Coordination Loop.
Perfect aesthetic match to the user's reference image in strict Black & White.
Features exact continuous arcs with flush geometric arrowheads.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "v2", "figures")
os.makedirs(OUT_DIR, exist_ok=True)
PDF_OUT = os.path.join(OUT_DIR, "fig_cps_loop.pdf")
PNG_OUT = os.path.join(OUT_DIR, "fig_cps_loop.png")

# ── Colors ────────────────────────────────────────────────────────────────────
BG_COL = "white"
TXT_COL = "black"

# ── Canvas ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7.4, 6.1), dpi=300)
fig.patch.set_facecolor(BG_COL)
ax.set_facecolor(BG_COL)
ax.set_aspect("equal")
ax.axis("off")
ax.set_xlim(-5.7, 5.7)
ax.set_ylim(-4.55, 4.62)

R_OUT = 3.3   # dashed outer ring
R_IN  = 2.7   # solid inner ring
DOT_R = 0.16  # radius of junction dots
GAP_DEG = 4.5 # angular gap to make room for the junction dots

# ── Fancy Arc Drawing Function ────────────────────────────────────────────────
def draw_arc_w_flush_arrow(ax, r, from_deg, to_deg, lw, is_dashed=False):
    """
    Draws a perfect arc ending exactly at an elegant geometric arrowhead.
    No lines undershooting or overshooting.
    """
    direction = 1 if to_deg > from_deg else -1
    
    # Arrow properties
    head_len = 0.22
    head_wid = 0.18
    # calculate angular length of the arrowhead along the arc
    # arc length = r * theta => theta_rad = arc_len / r
    head_arc_rad = head_len / r
    head_arc_deg = np.degrees(head_arc_rad)
    
    # The line should stop exactly at the base of the arrowhead
    line_end_deg = to_deg - (direction * head_arc_deg * 0.95)
    
    # Generate line arc points
    t = np.linspace(from_deg, line_end_deg, 200)
    x = r * np.cos(np.radians(t))
    y = r * np.sin(np.radians(t))
    
    # Plot the line
    if is_dashed:
        ax.plot(x, y, color=TXT_COL, lw=lw, dashes=(8, 4), zorder=2, solid_capstyle="butt")
    else:
        ax.plot(x, y, color=TXT_COL, lw=lw, zorder=2, solid_capstyle="butt")
        
    # Draw arrowhead
    angle_end = np.radians(to_deg)
    # The tangent is perpendicular to the radius
    dx = -np.sin(angle_end) * direction
    dy =  np.cos(angle_end) * direction
    
    # Tip of the arrow is exactly at `to_deg`
    tip_x = r * np.cos(angle_end)
    tip_y = r * np.sin(angle_end)
    head_tip = np.array([tip_x, tip_y])
    
    # Base of the arrow head
    head_base = head_tip - np.array([dx, dy]) * head_len
    
    # Normal to the tangent
    nx, ny = -dy, dx
    
    # Corner points of the arrow head
    p1 = head_base + np.array([nx, ny]) * (head_wid / 2)
    p2 = head_base - np.array([nx, ny]) * (head_wid / 2)
    
    poly = plt.Polygon([head_tip, p1, p2], color=TXT_COL, zorder=3)
    ax.add_patch(poly)

# Outer Ring (Clockwise, Dashed)
draw_arc_w_flush_arrow(ax, R_OUT, 90-GAP_DEG, 0+GAP_DEG, lw=2.5, is_dashed=True)
draw_arc_w_flush_arrow(ax, R_OUT, 0-GAP_DEG, -90+GAP_DEG, lw=2.5, is_dashed=True)
draw_arc_w_flush_arrow(ax, R_OUT, -90-GAP_DEG, -180+GAP_DEG, lw=2.5, is_dashed=True)
draw_arc_w_flush_arrow(ax, R_OUT, 180-GAP_DEG, 90+GAP_DEG, lw=2.5, is_dashed=True)

# Inner Ring (Counter-Clockwise, Solid)
draw_arc_w_flush_arrow(ax, R_IN, 0+GAP_DEG, 90-GAP_DEG, lw=3.3, is_dashed=False)
draw_arc_w_flush_arrow(ax, R_IN, 90+GAP_DEG, 180-GAP_DEG, lw=3.3, is_dashed=False)
draw_arc_w_flush_arrow(ax, R_IN, -180+GAP_DEG, -90-GAP_DEG, lw=3.3, is_dashed=False)
draw_arc_w_flush_arrow(ax, R_IN, -90+GAP_DEG, 0-GAP_DEG, lw=3.3, is_dashed=False)

# ── Junction dots (White fill, dark border) ───────────────────────────────────
for deg in [0, 90, 180, 270]:
    theta = np.radians(deg)
    for r in [R_OUT, R_IN]:
        ax.add_patch(plt.Circle((r*np.cos(theta), r*np.sin(theta)), DOT_R,
                                color="white", ec=TXT_COL, lw=1.8, zorder=5))

# ── Actor labels ──────────────────────────────────────────────────────────────
def actor(x, y, title1, title2, sub):
    t = title1 if not title2 else f"{title1}\n{title2}"
    
    ax.text(x, y + 0.12, t, ha="center", va="bottom",
            fontsize=12.5, fontweight="bold", color=TXT_COL, linespacing=1.0, zorder=8)
    ax.text(x, y - 0.10, sub, ha="center", va="top",
            fontsize=9.5, color=TXT_COL, linespacing=1.2, zorder=8)

actor(0.0,  3.9, "PROTOCOL RULES", "", "(Validate work / grant access)")
actor(0.0, -4.02, "END USERS", "", "(Consume the service / generate demand)")
actor(5.25,  0.0, "INFRASTRUCTURE", "PROVIDERS", "(Deploy and maintain\nphysical capacity)")
actor(-4.8, 0.0, "TOKEN LAYER", "", "(Payments, rewards,\nand governance)")

# ── Center annotation box ─────────────────────────────────────────────────────
msg = (
    "If one part of this loop weakens,\n"
    "the effects do not remain financial;\n"
    "they propagate directly into\n"
    "physical capacity and service quality."
)
ax.text(0, 0, msg, ha="center", va="center",
        fontsize=9.5, color=TXT_COL, linespacing=1.4,
        bbox=dict(boxstyle="square,pad=0.8", fc="white", ec=TXT_COL, lw=1.5),
        zorder=9)

# ── Save ──────────────────────────────────────────────────────────────────────
fig.subplots_adjust(left=0.035, right=0.965, top=0.975, bottom=0.025)
fig.savefig(PDF_OUT, format="pdf", bbox_inches="tight", dpi=300)
fig.savefig(PNG_OUT, format="png", bbox_inches="tight", dpi=300)
plt.close(fig)

print(f"Saved PDF: {PDF_OUT}")
print(f"Saved PNG: {PNG_OUT}")
