import { Pressable, ScrollView, StyleSheet, Text, View } from "react-native";

export default function Index() {
  return (
    <ScrollView style={style.container}>
      <View style={style.welcomingContainer}>
        <View style={style.text}>
          <Text style={style.welcomingText}>Accuratly Detect</Text>
          <Text style={style.welcomingText}>AI-Generated</Text>
          <Text style={style.welcomingText}>Content</Text>
        </View>
        <Text style={style.text}>Leverage advanced models to identify text from tools like ChatGPT, Gemini, and more. Ensure authenticity and maintain trust in your content.
        </Text>
        <Pressable style={style.button}> 
          <Text style={style.buttonText}>Try Detector</Text>
        </Pressable>
      </View>
      <View>
        <Text>Edit app/index.tsx to edit this screen.</Text>
      </View>
    </ScrollView>
    
  );
}

const style = StyleSheet.create({
  container: {
    flex: 1, // tells the component to take up all available space in its parent
    padding: 10

  },
  welcomingContainer: {
    flex: 1,
    justifyContent: "center",
    backgroundColor: "#ffffffff",
    height: "80%",
    fontWeight: 'bold'
  },
  welcomingText: {
    fontSize: 50,
    justifyContent: "center",
    flex: 1,
    fontWeight: 'bold',
  },
  
  button: {
    backgroundColor:"#0051ffff",
    alignItems: 'center',
    borderRadius: 8,
    paddingVertical: 20, // Padding is the space inside a component, between its content (like text) and its border/background.
    paddingHorizontal: 14,
  },
  buttonText: {
    color: "#FFFF",
    fontSize: 16

  },
  text: {
    justifyContent: 'center',
    alignItems: 'center',
  }
})
