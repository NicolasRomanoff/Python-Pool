

bar_chara = "█"
bar_len = 100


def ft_tqdm(lst: range):
    '''
    Display a loader with range defined at param1

    Args:
        param1 (range): A range for define the loader

    Yield:
        int: A number that indicates the progress of the loader
    '''
    for nb in lst:
        percentage = str(int((nb + 1) * 100 / lst.stop)).rjust(3)
        bar = "".ljust(
            int((nb + 1) * bar_len / lst.stop),
            bar_chara) \
            .ljust(bar_len)
        print(f"\r{percentage}%|{bar}| {nb + 1}/{lst.stop}", end='')
        yield nb
