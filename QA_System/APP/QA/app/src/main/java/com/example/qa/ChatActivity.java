package com.example.qa;

import android.content.Context;
import android.graphics.Color;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.text.SpannableString;
import android.text.Spanned;
import android.text.TextPaint;
import android.text.style.URLSpan;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;

import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

public class ChatActivity extends AppCompatActivity implements View.OnClickListener{

    ListView listView;
    EditText input_box;
    Button send_btn;
    List<MsgItem> msg_list;
    MsgAdapter msgAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams. FLAG_FULLSCREEN , WindowManager.LayoutParams. FLAG_FULLSCREEN);
        setContentView(R.layout.activity_chat);
        init();
        sendData(VALUES.HELLO,MsgItem.TYPE_ROBOT);
    }

    public void init(){
        listView = (ListView) findViewById(R.id.msg_list_view);
        input_box = (EditText) findViewById(R.id.input_box);
        send_btn = (Button) findViewById(R.id.send_btn);
        send_btn.setOnClickListener(this);

        msg_list = new ArrayList<MsgItem>();
        msgAdapter = new MsgAdapter(getBaseContext(),R.id.msg_list_view,msg_list);
        listView.setAdapter(msgAdapter);
    }

    void sendData(String msg,int type){
        MsgItem sendMsg= new MsgItem(msg,type);
        msg_list.add(sendMsg);
        msgAdapter.notifyDataSetChanged();
        //定位到listview尾部
        listView.setSelection(msg_list.size());
        listView.callOnClick();
        listView.invalidate();
    }

    private void startNetThread(final String msg) {
        new Thread() {
            public String result;
            public void run() {
                try {
                    //创建客户端对象
                    Socket socket = new Socket("10.17.145.7", 8080);
                    //获取客户端对象的输出流
                    OutputStream outputStream = socket.getOutputStream();
                    //把内容以字节流的形式写入(data).getBytes();
                    outputStream.write(msg.getBytes());
                    //刷新流管道
                    outputStream.flush();

                    //拿到客户端输入流
                    InputStream is = socket.getInputStream();
                    byte[] bytes = new byte[1024];
                    //回应数据
                    int n = is.read(bytes);
                    result = new String(bytes, 0, n);
                    System.out.println(result);
                    String[] ss=result.split("\n");
                    System.out.println(ss[0]);
                    System.out.println(ss[1]);
                    sendData(result,MsgItem.TYPE_ROBOT);

                    //关闭流
                    is.close();
                    //关闭客户端
                    socket.close();
                }catch (Exception e){
                    e.printStackTrace();
                }
            }
            //启动线程
        }.start();
    }

    boolean callRobot(String msg) {
        try {
            startNetThread(msg);
            return true;
        }catch (Exception e){
            e.printStackTrace();
        }
        return false;
    }

    @Override
    public void onClick(View v) {
        String msg = input_box.getText().toString();
        //Send when msg is not null
        if (msg.equals("")==false){
            sendData(msg,MsgItem.TYPE_USER);
            //清空输入框
            input_box.setText("");
            //隐藏键盘
            InputMethodManager imm = (InputMethodManager)
                    getSystemService(Context.INPUT_METHOD_SERVICE);
            imm.hideSoftInputFromWindow(v.getWindowToken(), 0);
            if(callRobot(msg) == false){
                //发送消息
                sendData(VALUES.ERROR,MsgItem.TYPE_ROBOT);
            }
        }
    }

    public class URLSpanNoUnderline extends URLSpan {

        public URLSpanNoUnderline(String url){
                super(url);
        }

        @Override
        public void updateDrawState(TextPaint ds){
            super.updateDrawState(ds);
            ds.setUnderlineText(false);
            ds.setColor(Color.BLUE);
        }
    }

}
