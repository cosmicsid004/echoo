import 'package:echoo/commonThings/common.dart';
import 'package:flutter/material.dart';

import 'firstPageUtilities.dart';

class registerPage extends StatefulWidget {
  const registerPage({super.key});

  @override
  State<registerPage> createState() => _registerPageState();
}

class _registerPageState extends State<registerPage> {

  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _username = TextEditingController();
  final TextEditingController _password = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: colors.backgroundColor(),
      appBar: AppBar(backgroundColor: colors.appBarColor()),
      body: Center(
        child: Container(
          padding: EdgeInsets.all(14),
          alignment: Alignment.center,
          height: 500, width: 400,
          decoration: BoxDecoration(color: const Color(0xFF222831), borderRadius: BorderRadius.circular(14), boxShadow: [containerShadow.shadow()],),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [

              Text("eecho", style: TextStyle(color: Colors.white, fontFamily: projectFonts.logoFont, fontSize: 100),),

              TextField(
                cursorOpacityAnimates: true,
                decoration: inputBoxDecoration.boxdecoration(label: "Email ID", icon: Icon(Icons.mail_outline)),
                style: inputBoxDecoration.textDecoration(),
                controller: _emailController,
              ),

              SizedBox(height: 12,),

              TextField(
                cursorOpacityAnimates: true,
                decoration: inputBoxDecoration.boxdecoration(label: "Username", icon: Icon(Icons.drive_file_rename_outline)),
                style: inputBoxDecoration.textDecoration(),
                controller: _username,
              ),

              SizedBox(height: 12,),

              TextField(
                obscureText: true,
                cursorOpacityAnimates: true,
                decoration: inputBoxDecoration.boxdecoration(label: "Password", icon: Icon(Icons.password)),
                style: inputBoxDecoration.textDecoration(),
                controller: _password,
              ),

              SizedBox(height: 12,),

              ElevatedButton(onPressed: () => {print("Email is ${_emailController.text}, Username is ${_username.text}, Password is ${_password.text}")},
                style: loginButtonStyle.style(),
                onLongPress: () => Navigator.pop(context),
                child: Text("Sign Up", style: TextStyle(fontFamily: projectFonts.buttonFonts),),
              ),

              SizedBox(height: 12,),

            ],
          ),
        ),
      ),
    );
  }
}
