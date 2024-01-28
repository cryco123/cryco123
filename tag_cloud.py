import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Read text from a file
file_path = 'fauzi.txt'  # Replace with the path to your text file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the generated word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
