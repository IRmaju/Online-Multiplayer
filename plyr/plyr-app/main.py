import streamlit as st

# Initialize players
if "players" not in st.session_state:
    st.session_state.players = [(100, 100), (300, 100)]

# Player selection
player_id = st.selectbox("Select your Player:", [0, 1], format_func=lambda x: f"Player {x+1}")
player_pos = list(st.session_state.players[player_id])

# Movement Buttons
st.write("Use buttons to move:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅️ Left"):
        player_pos[0] -= 5
with col2:
    if st.button("⬆️ Up"):
        player_pos[1] -= 5
with col3:
    if st.button("➡️ Right"):
        player_pos[0] += 5

if st.button("⬇️ Down"):
    player_pos[1] += 5

# Update position
st.session_state.players[player_id] = tuple(player_pos)

# Display players
st.header("Players Positions")

player_colors = ["Blue", "Red"]
for i, pos in enumerate(st.session_state.players):
    st.write(f"Player {i+1} ({player_colors[i]}): Position {pos}")

# Drawing Part (Optional Fancy Display)
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_xlim(0, 600)
ax.set_ylim(0, 400)
ax.invert_yaxis()

# Draw players
ax.add_patch(plt.Rectangle(st.session_state.players[0], 50, 50, color="blue"))
ax.add_patch(plt.Rectangle(st.session_state.players[1], 50, 50, color="red"))

st.pyplot(fig)

