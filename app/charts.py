import matplotlib.pyplot as plt
def generate_bar_chart(filename, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{filename}.png')

def generate_pie_chart(filename, labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig(f'./imgs/{filename}.png')


if __name__ == '__main__':
    generate_bar_chart('python_repos_bar', ['a', 'b', 'c'], [400,200,300])
    generate_pie_chart('python_repos_pie', ['a', 'b', 'c'], [400,200,300])
    print('Generating charts...')