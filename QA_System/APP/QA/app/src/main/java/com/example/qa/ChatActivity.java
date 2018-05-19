package com.example.qa;

import android.content.Context;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;

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
        callRobot(VALUES.HELLO);
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
    }

    StringBuffer sb;
    String getData(String msg){
        return "hhh";
    }

    boolean callRobot(String msg) {
        String data = getData(msg);
        if (data.equals("") == true) {
            sendData(VALUES.INTERNET_ERROR, MsgItem.TYPE_ROBOT);
            return false;
        }
        else if (data.equals("") == false) {
            sendData(data, MsgItem.TYPE_ROBOT);
            return true;
        }
        else return false;
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
}
