# ���� cookie:
response.set_cookie(
        key,     #��
        value,   #ֵ
        max_age, # ����Ϊ��λ��cookie���ʱ��
        expires, # ʧЧʱ�䣬����һ�� datetime �Ķ���
        path,    # �洢��·��
        )

# ��ȡ cookie
request.cookies.get('key')

# ɾ�� cookie
response.delete_cookie('key')
