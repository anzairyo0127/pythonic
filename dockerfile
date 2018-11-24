FROM python:3.6.6
# setting
ENV PYTHONUNBUFFERED 1
# pip インストールリストのコピー
COPY requirements.txt /tmp/requirements.txt
# インストールリストを用いたpipによるmoduleのダウンロード
RUN pip install -r /tmp/requirements.txt

RUN mkdir /var/share
WORKDIR /var/share