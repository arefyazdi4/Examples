import matplotlib.pyplot as plt


class RunTimeAlgorithmPlot:
    __doc__ = ''' creat obj then use speed_test function to give you ur graph
     function need a N -> reputation of func :int and algorithm func must return
       an integer that present number of performs'''

    fn_axis = []
    n_axis = []

    @staticmethod
    def perform(n, fn):
        RunTimeAlgorithmPlot.fn_axis.append(fn)
        RunTimeAlgorithmPlot.n_axis.append(n)

    @staticmethod
    def show_plot():
        plt.title('T(n)')
        plt.xlabel('N')
        plt.ylabel('f(n)')
        plt.plot(RunTimeAlgorithmPlot.n_axis, RunTimeAlgorithmPlot.fn_axis)
        plt.show()

    @staticmethod
    def speed_test(algorithm, n):
        RunTimeAlgorithmPlot.fn_axis.clear()
        RunTimeAlgorithmPlot.n_axis.clear()
        for i in range(n):
            fn = algorithm(i)
            RunTimeAlgorithmPlot.perform(i, fn)
        RunTimeAlgorithmPlot.show_plot()


def n3(n):
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count += 1
    return count


def n2(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count


def n1(n):
    count = 0
    for i in range(n):
        count += 1
    return count


if __name__ == '__main__':
    # RunTimeAlgorithmPlot.speed_test(n3, 100)
    # RunTimeAlgorithmPlot.speed_test(n2, 100)
    RunTimeAlgorithmPlot.speed_test(n1, 100)
