

# -----Answer-----
def shorten(s, k):
    return s[:k] + '...' if len(s) > k else s
