from email import message
from .models import Maintenance_Mail_Setting
from django.core.mail import send_mail


class MachineLogSendMail:
    
    def mail_send():
        
        object_list = Maintenance_Mail_Setting.objects.all()
        for log_i in object_list:
            if log_i.Maintenance_send_setting:
                if (log_i.Maintenance_threshold_time < log_i.Maintenance_machine_history.Machine_log_time0)or\
                    (log_i.Maintenance_threshold_time < log_i.Maintenance_machine_history.Machine_log_time1)or\
                    (log_i.Maintenance_threshold_time < log_i.Maintenance_machine_history.Machine_log_time2)or\
                    (log_i.Maintenance_threshold_time < log_i.Maintenance_machine_history.Machine_log_time3)or\
                    (log_i.Maintenance_threshold_time < log_i.Maintenance_machine_history.Machine_log_time4)or\
                    (log_i.Maintenance_threshold_time < log_i.Maintenance_machine_history.Machine_log_time5)or\
                    (log_i.Maintenance_threshold_time < log_i.Maintenance_machine_history.Machine_log_time6)or\
                    (log_i.Maintenance_threshold_time < log_i.Maintenance_machine_history.Machine_log_time7)or\
                    (log_i.Maintenance_threshold_time < log_i.Maintenance_machine_history.Machine_log_time8)or\
                    (log_i.Maintenance_threshold_time < log_i.Maintenance_machine_history.Machine_log_time9):
                    try:
                        subject = str(log_i.Maintenance_machine_history.Machine_model) + 'メンテナンス時期のお知らせ'                  
                        msg = str(log_i.Maintenance_mail_notification.Mail_name) + '様  \n' + str(log_i.Maintenance_machine_history.Machine_model) + 'の稼働時間がメンテナンス時期になりましたのでメールにてお知らせ致します。'
                        from_email = 'kenji1781@gmail.com'
                        to_mail = [str(log_i.Maintenance_mail_notification.Mail_address)]
                        send_mail(subject,msg,from_email,to_mail,fail_silently=False)
                        
                    except:
                        pass
    
