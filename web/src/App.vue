<template>
  <v-app>
    <Header />

    <v-container>
      <v-layout>
        <v-flex xs6>
          <DrawingBoard :drawnImage="drawnImage" />
        </v-flex>
        <v-flex xs6>
          <Predictions :chart-data="chartData" />
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>

<script>
import * as tf from '@tensorflow/tfjs';
import DrawingBoard from '@/components/DrawingBoard';
import Predictions from '@/components/Predictions';
import Header from '@/components/Header';

export default {
  name: 'App',
  components: {
    DrawingBoard,
    Predictions,
    Header
  },
  data() {
    return {
      model: tf.Model,
      predictions: [],
      chartData: null,
      randomImage: require('@/assets/test_data/img_1.jpg'),
      drawnImage: {
        image: null
      }
    };
  },
  created() {
    this.fillData();
  },
  methods: {
    /* TODO: Just for testing, remove... */
    generateRandomImage() {
      const randomNumber = Math.floor(Math.random() * 9) + 1;
      this.randomImage = require('@/assets/test_data/img_' +
        randomNumber +
        '.jpg');
      setTimeout(() => {
        this.predict();
      }, 100);
    },
    /* TODO: But in other component... */
    fillData() {
      this.chartData = {
        labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        datasets: [
          {
            label: 'Prediction',
            backgroundColor: '#f87979',
            data: this.predictions.map(prediction => prediction * 100)
          }
        ]
      };
    },
    async loadModel() {
      this.model = await tf.loadModel('http://localhost:5000/model');
    },
    async predictImage(imageData) {
      let image = tf.fromPixels(imageData, 1);
      image = image.reshape([1, 28, 28]);
      image = tf.cast(image, 'float32');

      console.log(image);

      const prediction = await this.model.predict(image);
      this.predictions = Array.from(prediction.dataSync());
      this.fillData();
    }
  },
  mounted() {
    this.loadModel();
  },
  watch: {
    'drawnImage.image': function() {
      this.drawnImage.image.width = 28;
      this.drawnImage.image.height = 28;
      this.predictImage(this.drawnImage.image);
    }
  }
};
</script>
