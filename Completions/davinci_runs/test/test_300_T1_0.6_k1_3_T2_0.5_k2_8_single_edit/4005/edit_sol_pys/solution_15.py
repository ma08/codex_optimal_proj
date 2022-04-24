/*
 * Copyright (c) 2017-present Muneeb Samuels. All Rights Reserved. See License.txt for license information.
 */

import { fromJS } from 'immutable'
import {
  GET_FILE_REQUEST,
  GET_FILE_SUCCESS,
  GET_FILE_FAILURE,
  SAVE_FILE_REQUEST,
  SAVE_FILE_SUCCESS,
  SAVE_FILE_FAILURE
} from 'actions/types'

const initialState = fromJS({
  file: {},
  isFetching: false,
  isSaving: false,
  error: null
})

export default (state = initialState, action) => {
  switch (action.type) {
    case GET_FILE_REQUEST:
      return state.merge({
        isFetching: true,
        error: null
      })
    case GET_FILE_SUCCESS:
      return state.merge({
        file: action.payload,
        isFetching: false,
        error: null
      })
    case GET_FILE_FAILURE:
      return state.merge({
        isFetching: false,
        error: action.payload
      })
    case SAVE_FILE_REQUEST:
      return state.merge({
        isSaving: true,
        error: null
      })
    case SAVE_FILE_SUCCESS:
      return state.merge({
        file: action.payload,
        isSaving: false,
        error: null
      })
    case SAVE_FILE_FAILURE:
      return state.merge({
        isSaving: false,
        error: action.payload
      })
    default:
      return state
  }
}
