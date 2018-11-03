import os

def add_comment(source):
    with open(source, 'r') as f:
        lines = f.readlines()
        problem_no, ext = os.path.splitext(os.path.basename(source))
        if ext == '.py':
            lines.insert(0,'\n')
            lines.insert(0,'# Problem: https://www.acmicpc.net/problem/{}\n'.format(problem_no))
            lines.insert(0,'\n')
            with open('_'.join(os.path.splitext(source)), 'x') as fd:
                fd.write(''.join(lines))


if __name__ == '__main__':
    # Dirty but for running only once
    # Get *python* folder's file list
    files = [os.path.join('python', path) for path in os.listdir(os.path.join(os.getcwd(),'python'))]
    # Add Problem link for each file
    [add_comment(i) for i in files]
    # remove original files
    [os.remove(os.path.join('python',s)) for s in os.listdir('python') if not '_' in s]
    # remove underbar in each file's name
    [os.rename('python/' + s, 'python/' + s[:-4]+'.py') for s in os.listdir('python')]


