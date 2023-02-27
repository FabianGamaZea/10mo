import 'package:flutter/material.dart';

// ignore: camel_case_types
class minimoScreen extends StatefulWidget {
  const minimoScreen({super.key});

  @override
  State<minimoScreen> createState() => _minimoScreenState();
}

// ignore: camel_case_types
class _minimoScreenState extends State<minimoScreen> {
  void resul(String variable) {
    setState(() {
      Text(variable);
      print("wea");
    });
  }

  @override
  Widget build(BuildContext context) {

    final TextEditingController textFieldController = TextEditingController();
    String myText ;

    return Scaffold(
      appBar: AppBar(
        title: const Text('minScreen'),
        //elevation: 10.0,
      ),
      backgroundColor: Colors.white,
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(
              controller: textFieldController,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                hintText: 'Enter a search term',
              ),
              onSubmitted: (value) {
                setState(() {
                  myText = value;
                  print(myText);
                  //resul(variable);
                });
              },
            ),
            
           // Text(myText),
          ],
        ),
      ),
        floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
        floatingActionButton: FloatingActionButton(
        child: const Icon(Icons.subdirectory_arrow_right_outlined),
        onPressed: () {
          setState(() {
            //print(myText);
          });

         },
       ),
    );
  }
}
