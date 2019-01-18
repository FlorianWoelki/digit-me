<template>
  <v-app>
    <img id="test-image" src="@/assets/test_data/img_1.jpg" width="28" height="28">
  </v-app>
</template>

<script>
import * as tf from '@tensorflow/tfjs';

export default {
  name: 'App',
  data() {
    return {
      model: tf.Model,
      predictions: []
    };
  },
  methods: {
    async loadModel() {
      const model = await tf.loadModel('http://localhost:5000/model');

      const imageData = document.querySelector('#test-image');
      let img = tf.fromPixels(imageData, 1);
      img = img.reshape([1, 28, 28]);
      img = tf.cast(img, 'float32');

      const prediction = model.predict(img);
      console.log(Array.from(prediction.dataSync()));
    }
    /*,
    async predict() {
      const pred = await tf.tidy(() => {
        const imageData = document.querySelector('#test-image');
        let img = tf.fromPixels(imageData, 1);
        img = img.reshape([1, 28, 28, 1]);
        img = tf.cast(img, 'float32');

        const output = this.model.predict(img);

        this.predictions = Array.from(output.dataSync());
      });
      return pred;
    }*/
  },
  mounted() {
    this.loadModel();
  }
};
</script>
