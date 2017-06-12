"""
#####Complete the method so that it does the following:

    Removes any duplicate query string parameters from the url
    Removes any query string parameters specified within the 2nd argument (optional array)

Examples:

stripUrlParams('www.codewars.com?a=1&b=2&a=2') // returns 'www.codewars.com?a=1&b=2'
stripUrlParams('www.codewars.com?a=1&b=2&a=2', ['b']) // returns 'www.codewars.com?a=1'
stripUrlParams('www.codewars.com', ['b']) // returns 'www.codewars.com'
"""

def strip_url_params(url, params_to_strip = []):
  if '?' not in url:
    return url
  work_list=list(url.split('?')[1])
  tmp=[]
  for i in work_list:
    if i not in tmp:
      tmp.append(i)
    else:
      del work_list[work_list.index(i):(work_list.index(i))+4]
  if len(params_to_strip) !=0:
    for i in tmp:
      if i in params_to_strip:
        del tmp[(tmp.index(i)-1):(tmp.index(i))+4]
  return url.split('?')[0]+'?'+''.join(tmp)
