<template>
  <div class="weather-component-container">
    <p id="weather-code-text">{{ weather?.weather_code }}</p>
    <p id="current-temperature">{{ weather?.temperature_2m }}°C</p>
    <div class="weather-list-items" v-for="[name, value] in filtered_weather" :key="name">
      <p class="weather-list-item-names">{{ name }}:</p>
      <div class="weather-list-item-values">
        <p>{{ value[0] }}</p>
        <p>{{ value[1] }}</p>
      </div>
    </div>
    <p id="location">{{ location }}</p>
  </div>
</template>

<script setup lang="ts">
  import {ref, onMounted, computed} from "vue";
  import apiClient from "@/api";

  interface WeatherResponse {
    weather_code: string,
    temperature_2m: number,
    apparent_temperature: number,
    wind_speed_10m: number,
    precipitation_probability: number,
    precipitation: number,
    uv_index_max: number,
    sunrise: string,
    sunset: string
  }

  const weather = ref<WeatherResponse>();
  const filtered_weather = ref<[string, any][]>([]);
  const location = ref<string>("");

  async function getWeather() {
    const response = await apiClient.get("/weather");
    weather.value = response.data;
    getFilteredWeather();
  }

  function getFilteredWeather() {
    if (weather.value) {
      filtered_weather.value = Object.entries(weather.value).slice(2);
    }
  }

  async function getLocation() {
    const response = await apiClient.get("/location");
    location.value = response.data;
  }

  onMounted(async () => {
    await getWeather();
    await getLocation();
  })
</script>

<style scoped>
  .weather-component-container {
    background-color: rgba(106, 106, 106, 0.5);
    border-radius: 25px;
    display: flex;
    flex-direction: column;
    padding: 2vh 2vw;
    align-items: center;
    width: 20vw;
  }

  #weather-code-text {
    font-weight: 700;
    font-size: x-large;
  }

  #current-temperature {
    font-weight: 900;
    font-size: xx-large;
  }

  .weather-list-items {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 100%;
  }

  .weather-list-item-names {
    font-weight: 700;
  }

  .weather-list-item-values {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 5vw;
  }

  #location {
    text-align: end;
    width: 100%;
    font-weight: 700;
    font-size: x-large;
  }
</style>

