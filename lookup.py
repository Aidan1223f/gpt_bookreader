def find_matches(chunks, keywords):
    df= {}
    results = {}
    trimmed_chunk = []

# trims off the overlap and looks at the middle of the chunk 
    padding = 500 
    for i, chunk in enumerate(chunks):
        if i != 0:
            chunk = chunk[padding:] 
        if i != len(chunks)-1:
            chunk = chunk[:-padding]     
        trimmed_chunk.append(chunk.lower()) 
        
# looks for the # of times keyword occurs in chunk, appends to dict df
    for chunk in chunks: 
        for keyword in keywords:
            occurences = chunk.count(keyword)
            if keyword not in df: 
                df[keyword] = 0
            df[keyword] += occurences

# looks for 
    for index,chunk in enumerate(trimmed_chunk):
        freq = 0
        for keyword in keywords:
            occurences = chunk.count(keyword)
            if df[keyword] > 0:
                freq += occurences / df[keyword]
            results[index] = freq


    return dict(sorted(results.items(), key=lambda item: item[1], reverse=True))