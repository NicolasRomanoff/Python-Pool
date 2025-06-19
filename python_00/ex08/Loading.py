

bar_chara = "█"
bar_len = 100


def ft_tqdm(lst: range):
    for nb in lst:
        percentage = str(int((nb + 1) * 100 / lst.stop)).rjust(3)
        bar = "".ljust(
            int((nb + 1) * bar_len / lst.stop),
            bar_chara) \
            .ljust(bar_len)
        print(f"\r{percentage}%|{bar}| {nb + 1}/{lst.stop}", end='')
        yield nb
