css = '''
<style>
.chat-message {
    padding:0.5rem; border-radius: 0.5rem: margin-bottom: 1rem; display: flex;
}
.chat-message.ana{
    background-color: #C7CBCA;
    border-radius: 10px;
    margin-top: 1rem;
    margin-bottom: 2rem;
}
.chat-message.ques{
    background-color: #5F6362;
    color: #fff;
    border-radius: 10px;
}
.chat-message.scorng{
    background-color: #d6470f;
    color: #fff;
    border-radius: 10px;
}
.chat-message.scorps{
    background-color: #1BBC94;
    color: #fff;
    border-radius: 10px;
}
.chat-message .avatar{
    width: 15%;
}
.chat-message .avatar img{
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message{
    padding: 0 1.5rem;
    bcolor: #fff;
}
'''

CV_template = '''
<div class="chat-message ques">
<div class="message">{{MSG}}</div>
</div>
'''

ANA_template = '''
<div class="chat-message ana">
<div class="message">{{MSG}}</div>
</div>
'''

SC_template_ng = '''
<div class="chat-message scorng">
<div class="message">{{MSG}}</div>
</div>
'''

SC_template_ps = '''
<div class="chat-message scorps">
<div class="message">{{MSG}}</div>
</div>
'''