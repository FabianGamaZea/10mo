import 'package:flutter/material.dart';

class minScreen extends StatelessWidget {
  const minScreen({super.key});

  @override
  Widget build(BuildContext context) {
    var sizeText = const TextStyle(fontSize: 30);
    int counter = 0;

    return Scaffold(
      appBar: AppBar(
        title: const Text('minScreen'),
        //elevation: 10.0,
      ),
      backgroundColor: Colors.white,
      body: Center(
        child: Row(
          children: [
            Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Text('Número de clicks', style: sizeText),
                  Text('$counter', style: sizeText),
                  const Padding(
                      padding:
                          EdgeInsets.symmetric(horizontal: 8, vertical: 16),
                      child: TextField(
                        obscureText: true,
                        decoration: InputDecoration(
                          border: OutlineInputBorder(),
                          labelText: 'Password',
                        ),
                      )),
                ],
              ),
            ),
          ],
        ),
      ),
      // floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
      // floatingActionButton: FloatingActionButton(
      //   child: const Icon(Icons.add),
      //   onPressed: () {
      //     ++counter;
      //   },
      // ),
    );
  }
}
