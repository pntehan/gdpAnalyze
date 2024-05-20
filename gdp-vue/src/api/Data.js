import { get } from "../utils/request"

export const getGDPData = query => {
    return get("/data/getGDPData", query)
  }
