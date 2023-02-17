import 'package:flutter/material.dart';

class minScreen extends StatefulWidget {
  const minScreen({Key? key}) : super(key: key);

  @override
  State<minScreen> createState() => _minScreenState();
}

class _minScreenState extends State<minScreen> {
  @override
  Widget build(BuildContext context) {
    var sizeText = TextStyle(fontSize: 30);
    int counter = 0;
    String _valueTextfield ="";

    return Scaffold(
      appBar: AppBar(
        title: const Text('minScreen'),
        //elevation: 10.0,
      ),
      backgroundColor: Colors.white,
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('Número de clicks', style: sizeText),
            Text('$counter', style: sizeText),
            Row(
              // ignore: prefer_const_literals_to_create_immutables
              children: [
                const Text('wea'),
                TextField(
                  decoration: const InputDecoration(
                    border: OutlineInputBorder(),labelText: 'entrada'),
                    onSubmitted: (value){
                      setState(() {
                        _valueTextfield = value;
                      });
                    },
      
                ),
              ],
            )
          ],
        ),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
      floatingActionButton: FloatingActionButton(
        child: const Icon(Icons.add),
        onPressed: () {
          ++counter;
        },
      ),
    );
  }
}
