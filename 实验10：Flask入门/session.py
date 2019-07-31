from flask import session
from datetime import timedelta

# ���� session
@app.route('/set_session')
def set_session():
    session.permanent=True # ����session�ĳ־û�
    app.permanent_session_lifetime=timedelta(minutes=5)  # ����session�Ĵ��ʱ��Ϊ5����
    session['username']='shixiaolou'
    return '�ɹ�����session'

# ��ȡ session
@app.route('/get_session')
def get_session():
    value = session.get('username')
    return '��ȡ��sessionֵΪ{}'.format(value)

# �Ƴ� session
@app.route('/del_session')
def del_session():
    value = session.pop('username')
    return '�ɹ����Ƴ�session,��ֵΪ{}'.format(value)
