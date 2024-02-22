import numpy as np
import plotly.express as px
import warnings

def simulate_dice_roll(num_simulations, num_faces, asymmetric=False):
    results = []
    for _ in range(num_simulations):
        if asymmetric:
            dice1 = np.random.randint(1, num_faces + 1)
            dice2 = np.random.randint(1, num_faces + 1)
        else:
            dice1 = np.random.randint(1, num_faces + 1)
            dice2 = np.random.randint(1, num_faces + 1)
            dice2 = num_faces + 1 - dice2  # Symmetric transformation

        results.append(dice1 + dice2)

    return results

# Параметри симуляції
num_simulations = 10000
num_faces = 27  # N = n + 3
asymmetric_simulation = simulate_dice_roll(num_simulations, num_faces, asymmetric=True)
symmetric_simulation = simulate_dice_roll(num_simulations, num_faces, asymmetric=False)

warnings.simplefilter(action='ignore', category=FutureWarning)

# Побудова гістограми за допомогою Plotly
fig = px.histogram(
    x=[asymmetric_simulation, symmetric_simulation],
    nbins=2 * num_faces + 1,
    labels={'x': 'Sum of Dice Rolls'},
    title='Dice Roll Simulation',
    color_discrete_sequence=['red', 'blue'],
    opacity=0.7,
)

# Включення попередження для інших частин коду, якщо необхідно
warnings.resetwarnings()

# Збереження гістограми у вигляді HTML-сторінки
fig.write_html('dice_simulation.html')

