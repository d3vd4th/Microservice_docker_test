import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  SafeAreaView,
  Dimensions,
} from 'react-native';
import Svg, { Path, Circle, G, Rect } from 'react-native-svg';

const { width } = Dimensions.get('window');

const MicrophoneIcon = () => (
  <Svg width="24" height="24" viewBox="0 0 24 24" fill="white">
    <Path d="M12 15c2.21 0 4-1.79 4-4V5c0-2.21-1.79-4-4-4S8 2.79 8 5v6c0 2.21 1.79 4 4 4zm-2-9c0-1.1.9-2 2-2s2 .9 2 2v6c0 1.1-.9 2-2 2s-2-.9-2-2V6z" />
    <Path d="M19 11h-1.7c0 3-2.54 5.1-5.3 5.1S6.7 14 6.7 11H5c0 3.41 2.72 6.23 6 6.72V21h2v-3.28c3.28-.49 6-3.31 6-6.72z" />
  </Svg>
);

const WaveBackground = () => (
  <Svg width={width} height="200" viewBox="0 0 400 200">
    <Path
      d="M0 50 Q100 0 200 50 T400 50 L400 200 L0 200 Z"
      fill="#6C63FF"
      opacity="0.1"
    />
  </Svg>
);

const LaunchScreen1 = ({ navigation }) => {
  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <WaveBackground />
        <View style={styles.illustration}>
          {/* Placeholder for character illustration */}
          <View style={styles.micIconContainer}>
            <MicrophoneIcon />
          </View>
        </View>
      </View>

      <View style={styles.content}>
        <Text style={styles.title}>Transform Speech into{'\n'}Text Effortlessly</Text>
        <Text style={styles.subtitle}>
          Capture every detail with RecogNotes.{'\n'}
          Record conversations, lectures, meetings, and{'\n'}
          more, and watch as they are transcribed into{'\n'}
          accurate text instantly.
        </Text>

        <View style={styles.dotContainer}>
          {[0, 1, 2, 3].map((_, index) => (
            <View
              key={index}
              style={[
                styles.dot,
                index === 0 ? styles.activeDot : null,
              ]}
            />
          ))}
        </View>
      </View>

      <View style={styles.buttonContainer}>
        <TouchableOpacity
          style={styles.registerButton}
          onPress={() => navigation.navigate('Register')}
        >
          <Text style={styles.registerText}>Register</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.signInButton}
          onPress={() => navigation.navigate('SignIn')}
        >
          <Text style={styles.signInText}>Sign in</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
};