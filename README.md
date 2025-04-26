# 🎮 Streamlit Player Movement Game

Welcome to the **Streamlit Player Movement Game**! 🎮 This app lets you control two players on a 2D plane, represented as colored rectangles. Use the interactive buttons to move players and see their positions update in real-time.

---

## 🌟 Features

- **Two Players**: Player 1 (Blue) and Player 2 (Red).
- **Interactive Movement**: Move players up, down, left, or right using simple buttons.
- **Real-Time Position Update**: See the positions of both players update instantly on the screen.
- **Player Selection**: Select which player you want to control.

---

## 🚀 How to Use

1. **Install the Required Packages**:
   
   Ensure you have the necessary packages installed by running the following command:

   ```bash
   pip install streamlit matplotlib
if "players" not in st.session_state:
    st.session_state.players = [(100, 100), (300, 100)]
player_id = st.selectbox("Select your Player:", [0, 1], format_func=lambda x: f"Player {x+1}")
fig, ax = plt.subplots()
ax.set_xlim(0, 600)
ax.set_ylim(0, 400)
ax.invert_yaxis()  # Y-axis inversion for graphical correctness
ax.add_patch(plt.Rectangle(st.session_state.players[0], 50, 50, color="blue"))
ax.add_patch(plt.Rectangle(st.session_state.players[1], 50, 50, color="red"))
st.pyplot(fig)

