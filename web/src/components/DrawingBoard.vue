<template>
  <div>
    <v-stage ref="stage" :config="stageSize">
      <v-layer ref="layer">
        <v-image 
          ref="image"
          :config="{
            image: canvas,
            x: x,
            y: y,
            stroke: stroke
          }"
          @mousedown="handleMouseDown"
          @mouseup="handleMouseUp"
          @mousemove="handleMouseMove"
        >
        </v-image>
      </v-layer>
    </v-stage>

    <div class="text-xs-center">
      <v-btn color="info" @click="handleErase">Erase</v-btn>
    </div>
  </div>
</template>

<script>
const width = window.innerWidth;
const height = window.innerHeight;

export default {
  props: ['drawnImage'],
  data() {
    return {
      canvas: null,
      context: null,
      isDrawing: false,
      lastPointerPosition: null,
      stageSize: {
        width: width,
        height: height
      },
      image: null,
      x: width / 12,
      y: height / 12 - 25,
      stroke: '#ff4d4d'
    };
  },
  methods: {
    handleErase() {
      this.isDrawing = false;
      this.drawnImage.image = null;

      this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
      this.$refs.layer.getStage().batchDraw();
    },
    handleMouseDown() {
      this.isDrawing = true;
      const stage = this.$refs.stage.getStage();
      this.lastPointerPosition = stage.getPointerPosition();
    },
    handleMouseUp() {
      this.isDrawing = false;

      let image = new Image();
      image.id = 'image-id';
      image.src = this.canvas.toDataURL();
      this.drawnImage.image = image;
    },
    handleMouseMove() {
      if (!this.isDrawing) {
        return;
      }

      this.context.globalCompositeOperation = 'source-over';

      this.context.beginPath();

      let localPosition = {
        x: this.lastPointerPosition.x - this.$refs.image.getStage().getX(),
        y: this.lastPointerPosition.y - this.$refs.image.getStage().getY()
      };
      this.context.moveTo(localPosition.x, localPosition.y);

      let position = this.$refs.stage.getStage().getPointerPosition();
      localPosition = {
        x: position.x - this.$refs.image.getStage().getX(),
        y: position.y - this.$refs.image.getStage().getY()
      };
      this.context.lineTo(localPosition.x, localPosition.y);
      this.context.closePath();
      this.context.stroke();

      this.lastPointerPosition = position;
      this.$refs.layer.getStage().batchDraw();
    }
  },
  mounted() {
    const canvas = document.createElement('canvas');
    canvas.width = this.stageSize.width / 4;
    canvas.height = this.stageSize.height / 2;

    const context = canvas.getContext('2d');
    context.strokeStyle = 'gray';
    context.lineJoin = 'round';
    context.lineWidth = 10;

    this.canvas = canvas;
    this.context = context;
  }
};
</script>

<style>
.info {
  margin-top: -500px;
}
</style>
