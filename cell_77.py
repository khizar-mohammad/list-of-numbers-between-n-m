#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x = []
for i in range(2000,3201):
  if i % 5 == 0:
    continue
  if i % 7 == 0:
    x.append(i)

print(*x,sep=",")

