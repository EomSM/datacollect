#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('주피터 서버에 오신 것을 환영합니다')


# In[5]:


print('2nd cell')


# # 내가 주석(큰제목)@ MarkDOwn 여기에 설명 쓰기

# ## 나는 누구 여긴 어디(중제목), @Markdown. 주석보다는 마크다운에 설명.

# ### 소제목? 되네

# * 나는 누구지
# * 나는 두번째 목록(마크다운에서의 목록 * )
# * 세번째
# 

# ** 더 작은 목록 
# ** 더 작은 목록22

# # 제일 큰 제목
# ## 그 다음 작은 제목
# ### 그다음

# * 아침
# * 점심
# * 저녁
#     * 밥밥밥
#     * 밥밥바밥 

# *이탤릭*
# **볼드**
# ***볼드&이탤릭***

# In[4]:


import pandas as pd


# In[5]:


df_2010 = pd.read_csv("../data/2010.csv", encoding='utf-8')


# In[6]:


df_2010


# In[7]:


df_2011=pd.read_csv("../data/2011.csv", encoding='utf-8')


# In[8]:


df_2011


# In[9]:


df_2012 = pd.read_csv("../data/2012.csv", encoding='utf-8')


# In[10]:


df_2012


# In[11]:


total_score=pd.concat([df_2010, df_2011, df_2012], ignore_index = True)


# In[12]:


total_score


# In[13]:


total_score.iloc[:,0] # iloc[행< 무조건 필요, 열]


# In[22]:


cc1=pd.read_csv("../data/concat_1.csv", encoding='utf-8')


# In[23]:


cc1


# In[25]:


cc2=pd.read_csv("../data/concat_2.csv", encoding='utf-8')


# In[27]:


cc3=pd.read_csv("../data/concat_3.csv", encoding='utf-8')


# In[26]:


cc2


# In[28]:


cc3


# In[35]:


ccall=pd.concat([cc1, cc2, cc3], sort=True, ignore_index=True)


# In[36]:


ccall #자동 인덱싱 붙여서 해


# In[37]:


ccall.iloc[1,1] 


# In[40]:


c1=ccall.loc[2] #2행 2번 row


# In[41]:


c1


# In[43]:


c2= ccall.iloc[:,0] #0열 0번 칼럼


# In[44]:


c2


# In[45]:


c3= ccall.iloc[:,4] #4열 4번 칼럼


# In[47]:


c3


# In[48]:


c4= ccall.loc[6:8] #6행~8행


# In[49]:


c4


# In[50]:


c5= ccall.iloc[:, 3:8] #3~8칼럼


# In[51]:


c5


# In[52]:


row_append = cc1.append(cc2, ignore_index= True)


# In[53]:


row_append


# In[54]:


type(row_append)


# In[55]:


row_append.columns


# In[58]:


inner_result=pd.concat([cc1, cc3], join='inner')


# In[59]:


inner_result #cc1, 3의 공통된 것을 가지고 합치기


# In[60]:


covid19=pd.read_csv("../data/country_wise_latest.csv")
covid19


# In[ ]:




