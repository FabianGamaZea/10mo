import 'package:flutter/material.dart';
//import 'package:pag_web/screen/min.dart';
import 'package:pag_web/screen/mini.dart';

void main() {
 runApp( const MyApp()) ;
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
   
   return const MaterialApp(
    debugShowCheckedModeBanner: false,      //Desaparece la etiqueta debug
    home: minScreen()
    //home:CounterScreen()
   // home:MyDataTable()
   );
  }
  

}
