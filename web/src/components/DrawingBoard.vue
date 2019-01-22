<template>
  <div class="drawing-board">
    <canvas
      id="canvas"
      @mousedown="handleMouseDown"
      @mouseup="handleMouseUp"
      @mousemove="handleMouseMove"
      width="400px"
      height="400px">
    </canvas>
  </div>
</template>

<script>
export default {
  name: 'DrawingBoard',
  data() {
    return {
      mouse: {
        current: {
          x: 0,
          y: 0
        },
        previous: {
          x: 0,
          y: 0
        },
        down: false
      }
    };
  },
  methods: {
    draw() {
      if (this.mouse.down) {
        const canvas = document.getElementById('canvas');
        const context = canvas.getContext('2d');
        context.clearRect(0, 0, 800, 800);

        context.lineTo(this.currentMouse.x, this.currentMouse.y);
        context.strokeStyle = 'black';
        context.lineWidth = 2;
        context.stroke();
      }
    },
    handleMouseDown() {
      this.mouse.down = true;
      this.mouse.current = {
        x: event.pageX,
        y: event.pageY
      };

      const canvas = document.getElementById('canvas');
      const context = canvas.getContext('2d');

      context.moveTo(this.currentMouse.x, this.currentMouse.y);
    },
    handleMouseUp() {
      this.mouse.down = false;
    },
    handleMouseMove(event) {
      this.mouse.current = {
        x: event.pageX,
        y: event.pageY
      };

      this.draw();
    }
  },
  mounted() {
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    context.translate(0.5, 0.5);
    context.imageSmoothingEnabled = false;
  },
  computed: {
    currentMouse() {
      const canvas = document.getElementById('canvas');
      const rect = canvas.getBoundingClientRect();
      return {
        x: this.mouse.current.x - rect.left,
        y: this.mouse.current.y - rect.top
      };
    }
  }
};
</script>

<style lang="css">
.drawing-board canvas {
  background: white;
  box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.2);
}
</style>
