import { get, post } from "../utils/request"

export const getGDPData = query => {
  return get("/data/getGDPData", query)
}

export const predict = query => {
  return post("/data/predict", query)
}
