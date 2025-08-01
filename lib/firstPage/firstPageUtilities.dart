import 'package:echoo/commonThings/common.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class containerShadow {
  static BoxShadow shadow() {
    return BoxShadow(
      color: Colors.white.withOpacity(0.5),
      blurRadius: 10,
      spreadRadius: 1,
      offset: const Offset(5, 5)
    );
  }
}

class inputBoxDecoration {
  static InputDecoration boxdecoration({required String label, required Icon icon}) {
    return InputDecoration(
        labelText: label,
        labelStyle: TextStyle(color: Color(0xFFAEAEAE)),
        icon: Icon(icon.icon, color: colors.iconColor(),),
        enabledBorder: OutlineInputBorder(
            borderSide: BorderSide(color: Color(0xFFEEEEEE), width: 1),
            borderRadius: BorderRadius.circular(12)
        ),
        focusedBorder: OutlineInputBorder(
            borderSide: BorderSide(color: Color(0xFFDFD0B8), width: 2),
            borderRadius: BorderRadius.circular(14)
        ),
        fillColor: Color(0xFF31363F), filled: true
    );
  }

  static TextStyle textDecoration() {
    return TextStyle(
      color: Colors.white
    );
  }
}

class loginButtonStyle {
  static ButtonStyle style() {
    return ButtonStyle(
      backgroundColor: MaterialStateProperty.all(Color(0xFF948979)),
      foregroundColor: MaterialStateProperty.all(Colors.white),
      overlayColor: MaterialStateProperty.all(Color(0xFFDFD0B8)),
      enableFeedback: true,
    );
  }
}