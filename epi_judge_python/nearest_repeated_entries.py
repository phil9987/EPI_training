from test_framework import generic_test


def find_nearest_repetition(paragraph):
    lookup = {}
    overall_min_dist = len(paragraph)
    for pos, word in enumerate(paragraph):
        if word in lookup:
            last_occ, min_dist = lookup[word]
            lookup[word] = (pos, min(min_dist, pos - last_occ))
            overall_min_dist = min(overall_min_dist, pos - last_occ)
        else:
            lookup[word] = (pos, len(paragraph))
    if overall_min_dist == len(paragraph):
        overall_min_dist = -1
    return overall_min_dist


if __name__ == '__main__':
    find_nearest_repetition( ["foo", "bar", "widget", "foo", "widget", "widget", "adnan"])
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
