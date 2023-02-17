import 'package:flutter/material.dart';
//import 'package:pag_web_1/screen/min.dart';
import 'package:pag_web_1/screen/minimo.dart';


void main() {
 runApp( const MyApp()) ;
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
   
   return const MaterialApp(
    debugShowCheckedModeBanner: false,      //Desaparece la etiqueta debug
    home: minimoScreen()
    //home: MyWidget()
    //home:CounterScreen()
   // home:MyDataTable()
   );
  }
  

}
