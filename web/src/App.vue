<template>
  <v-app>
    <img id="test-image" :src="randomImage" width="28" height="28">
    <v-btn
      color="info"
      @click="handleShuffle"
    >Shuffle</v-btn>
    <p>{{this.predictions}}</p>

    <DrawingBoard></DrawingBoard>

    <Predictions></Predictions>
  </v-app>
</template>

<script>
import * as tf from '@tensorflow/tfjs';
import DrawingBoard from '@/components/DrawingBoard';
import Predictions from '@/components/Predictions';

export default {
  name: 'App',
  components: {
    DrawingBoard,
    Predictions
  },
  data() {
    return {
      model: tf.Model,
      predictions: [],
      randomImage: require('@/assets/test_data/img_1.jpg')
    };
  },
  methods: {
    handleShuffle() {
      const randomNumber = Math.floor(Math.random() * 9) + 1;
      this.randomImage = require('@/assets/test_data/img_' +
        randomNumber +
        '.jpg');
      setTimeout(() => {
        this.predict();
      }, 100);
    },
    async loadModel() {
      this.model = await tf.loadModel('http://localhost:5000/model');
      this.predict();
    },
    async predict() {
      const imageData = document.querySelector('#test-image');
      let img = tf.fromPixels(imageData, 1);
      img = img.reshape([1, 28, 28]);
      img = tf.cast(img, 'float32');

      const prediction = await this.model.predict(img);
      this.predictions = Array.from(prediction.dataSync());
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
    //this.loadModel();
  }
};
</script>
