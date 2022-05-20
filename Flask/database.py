#!/usr/bin/env python
# coding: utf-8

# In[2]:


# !pip install pymysql


# In[4]:


import pymysql


# In[14]:


conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', charset='utf8')


# In[15]:


cursor = conn.cursor()


# In[16]:


cursor.execute('show databases;')


# In[17]:


result = cursor.fetchall()


# In[18]:


print(result)


# In[10]:


sql = 'create database if not exists falsk_db;'


# In[13]:


cursor.execute(sql)


# In[22]:


cursor.execute('use falsk_db;')


# In[25]:


sql="""
create table if not exists member(
`id` int(11) not null auto_increment,
`userid` varchar(50) not null,
`pwd` varchar(200) not null,
`name` varchar(20) default null,
`email` varchar(50) default null,
`regdate` datetime default null,
primary key(`id`)
)
"""

cursor = conn.cursor()
cursor.execute(sql)


# In[34]:


sql = """
insert into member values 
(1, 'aaa', '1234', '아이유', 'aaa@aaa.co.kr', '2019-06-24'),
(2, 'bbb', '1234', '방탄소년', 'bbb@bbb.co.kr', '2019-06-24')
"""

cursor.execute(sql)


# In[35]:


cursor.execute('select*from member;')
result = cursor.fetchall()
result


# In[36]:


sql = """
create table if not exists point_table (
`point_stu_idx` int(11) default null,
`point_stu_grade` varchar(50) default null,
`point_stu_kor` varchar(50) default null
)
"""
cursor.execute(sql)


# In[37]:


cursor.execute('select*from point_table;')
result = cursor.fetchall()
result


# In[38]:


sql = """
insert into point_table values
(2, '2', '90'),
(2, '3', '94'),
(1, '1', '89');
"""
cursor.execute(sql)


# In[39]:


cursor.execute('select*from point_table;')
result = cursor.fetchall()
result


# In[40]:


sql = """
CREATE TABLE IF NOT EXISTS student_table (
  `stu_idx` int(11) NOT NULL AUTO_INCREMENT,
  `stu_name` varchar(50) DEFAULT NULL,
  `stu_age` varchar(3) DEFAULT NULL,
  `stu_addr` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`stu_idx`)
) ;
"""
cursor.execute(sql)


# In[41]:


sql = """
INSERT INTO student_table (`stu_idx`, `stu_name`, `stu_age`, `stu_addr`) VALUES
   (1, '홍길동', '18', '서울시'),
   (2, '김개똥', '19', '서울시');
"""
cursor.execute(sql)


# In[42]:


cursor.execute('select*from student_table;')
result = cursor.fetchall()
result


# In[43]:


conn.commit()


# In[44]:


conn.close()


# In[ ]:





# In[45]:


def get_connection():

    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', charset='utf8')
    return conn


# In[46]:


conn = get_connection()


# In[47]:


cursor = conn.cursor()


# In[48]:


cursor.execute('show databases;')


# In[49]:


cursor.execute('use falsk_db;')


# In[51]:


sql = """
select stu_idx, stu_name, stu_age, stu_addr from student_table where stu_name like {};
""".format(name)

cursor.execute(sql)
result = cursor.fetchall()
result


# In[64]:


def get_student_list(stu_name):
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('use falsk_db;')
    
    
    sql = """
    select stu_idx, stu_name, stu_age, stu_addr from student_table
    """
    if stu_name != None and len(stu_name) > 0:
        sql += ' where stu_name like %s'
        
    sql += ' order by stu_idx desc;'
        
 
    if stu_name != None and len(stu_name) > 0:
        cursor.execute(sql, (f'%{stu_name}%'))
    else:
        cursor.execute(sql)
        
    result = cursor.fetchall()
    
    temp_list = []
    
    for row in result :
        temp_dict = {}
        temp_dict['stu_idx'] = row[0]
        temp_dict['stu_name'] = row[1]
        temp_dict['stu_age'] = row[2]
        temp_dict['stu_addr'] = row[3]
        
        temp_list.append(temp_dict)
        
    conn.close()
    
    return temp_list


# In[66]:


student_list = get_student_list([])
student_list


# In[67]:


# db 추가

def add_student(stu_name, stu_age, stu_addr):
    sql = """
    insert into student_table (stu_name, stu_age, stu_addr) values
    (%s, %s, %s)
    """
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('use falsk_db;')
    
    cursor.execute(sql, (stu_name, stu_age, stu_addr))
    conn.commit()
    
    sql2 = 'select max(stu_idx) from student_table'
    cursor.execute(sql2)
    result = cursor.fetchone()
    idx = result[0]
    
    conn.close()
    
    return idx


# In[68]:


add_student('김수로', 35, '인천')


# In[69]:


student_list = get_student_list([])
student_list


# In[70]:


# def get_student_info(stu_idx):
#     sql = """
#     select stu_name, stu_age, stu_addr, from student_table where stu_idx=%s
#     """
    
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute('use falsk_db;')
    
#     cursor.execute(sql, (stu_idx))
#     result = cursor.fetchone()
    
#     result_dic = {}
#     result_dic['stu_idx'] = stu_idx
#     result_dic['stu_name'] = result[0]
#     result_dic['stu_age'] = result[1]
#     result_dic['stu_addr'] = result[2]
    
#     conn.close()
    
#     return result_dic


# In[72]:


def get_student_info(stu_idx):
    sql = """
    select stu_name, stu_age, stu_addr from student_table where stu_idx=%s
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('use falsk_db;')     
    
    cursor.execute(sql, (stu_idx))
    result = cursor.fetchone()
    
    result_dic = {}
    result_dic['stu_idx'] = stu_idx
    result_dic['stu_name'] = result[0]
    result_dic['stu_age'] = result[1]
    result_dic['stu_addr'] = result[2]
    
    conn.close()
    
    return result_dic


# In[73]:


get_student_info(3)


# In[75]:


def add_point(point_stu_idx, point_stu_grade, point_stu_kor):
    
    sql = """
    insert into point_table values(%s, %s, %s)
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('use falsk_db;') 
    
    cursor.execute(sql, (point_stu_idx, point_stu_grade, point_stu_kor))
    
    conn.commit()
    
    conn.close()


# In[76]:


add_point(3,'5','100')


# In[77]:


def get_point(stu_idx):
    sql = """
    select point_stu_grade, point_stu_kor from point_table
    where point_stu_idx = %s order by point_stu_grade;
    """
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('use falsk_db;') 
    
    cursor.execute(sql, (stu_idx))
#     cursor.execute(sql.format(stu_idx))

    result = cursor.fetchall()
    
    result_list = []
    
    for result_dic in result:
        temp_dic = {}
        temp_dic['point_stu_grade'] = result_dic[0]
        temp_dic['point_stu_kor'] = result_dic[1]
        
    conn.close()
    
    return result_list


# In[79]:


get_point(1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




