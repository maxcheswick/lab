FROM ubuntu:22.04

RUN apt-get update && apt-get install -y openssh-server python3 \
    && mkdir /var/run/sshd

RUN useradd -m ansible && echo "ansible:ansible" | chpasswd \
    && mkdir -p /home/ansible/.ssh

COPY authorized_keys /home/ansible/.ssh/authorized_keys
RUN chown -R ansible:ansible /home/ansible/.ssh && chmod 600 /home/ansible/.ssh/authorized_keys

COPY sshd_config /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
