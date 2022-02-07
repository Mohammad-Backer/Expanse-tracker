def display():
    for i in tasks:
        print(i)

def add(task):
    tasks.append(task)


def finish(finished_task):
    for i in tasks:
        if i == finished_task:
            tasks.remove(i)

if __name__ == '__main__':
    try:
        with open('to_do.txt', 'r') as f:
            tasks = f.readlines()
            f.close()
    except:
        tasks = []
    while True:
        display()
        task = input('What do you want to do?')
        if task == 'exit':
            break
        elif task == 'finish':
            finished_task = input('What did you finish?')
            finish(finished_task)
            with open('to_do.txt', 'w') as f:
                for i in tasks:
                    st = i + '\n'
                    f.write(st)
                f.close()
        else : 
            add(task)
            with open('to_do.txt', 'a') as f:
                st = tasks[-1] + '\n'
                f.write(st)
                f.close()

        