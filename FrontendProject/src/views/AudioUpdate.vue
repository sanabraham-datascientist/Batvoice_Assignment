<template>
  <div class="container mx-auto mt-12">
         <Transcriptions/> 
  </div> 
  
</template>

<script>
import Transcriptions from "@/components/Transcriptions.vue";
import axios from "axios";
export default {
  name: "AudioUpdateView",
  components: {
    Transcriptions,
  },
};
//   data() {
//     return {
//       audioList: [],
//     };
//   },
//   mounted() {
//     this.getAudioList();
//   },
//   methods: {
//     getAudioList() {
//       axios
//         .get("/api")
//         .then((response) => {
//           console.log("data", response.data);
//           this.audioList = response.data;
//         })
//         .catch((error) => {
//           console.log("error", error);
//         });
//     },
//   },
// };
</script>
