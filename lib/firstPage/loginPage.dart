import 'package:echoo/commonThings/common.dart';
import 'package:echoo/firstPage/registerPage.dart';
import 'package:flutter/material.dart';
import 'firstPageUtilities.dart';

class loginPage extends StatefulWidget {
  const loginPage({super.key});

  @override
  State<loginPage> createState() => _loginPageState();
}

class _loginPageState extends State<loginPage> {

  final TextEditingController _emailController = TextEditingController();
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
          height: 400, width: 400,
          decoration: BoxDecoration(color: const Color(0xFF222831), borderRadius: BorderRadius.circular(14), boxShadow: [containerShadow.shadow()],),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [

              Text("eecho", style: TextStyle(color: Colors.white, fontFamily: projectFonts.logoFont, fontSize: 100),),

              TextField(
                cursorOpacityAnimates: true,
                decoration: inputBoxDecoration.boxdecoration(label: "Email", icon: Icon(Icons.person)),
                style: inputBoxDecoration.textDecoration(),
                controller: _emailController,
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

              ElevatedButton(onPressed: () => {print("Email is ${_emailController.text}, Password is ${_password.text}")},
                style: loginButtonStyle.style(),
                onLongPress: () => Navigator.push(context, MaterialPageRoute(builder: (context) => registerPage())),
                child: Text("Login", style: TextStyle(fontFamily: projectFonts.buttonFonts),),
              ),

              SizedBox(height: 12,),

              Text("Long press Login button to SignUp", style: TextStyle(color: Colors.white),)

            ],
          ),
        ),
      ),
    );
  }
}
