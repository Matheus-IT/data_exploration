from timeit import default_timer as timer


class Timer:
    def __enter__(self):
        self.start = timer()
        return self

    def __exit__(self, *exc_info):
        end = timer()
        print(end - self.start)
