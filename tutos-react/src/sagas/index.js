import { fork, all } from 'redux-saga/effects';

import {
  watchLoginStarted,
  watchRefreshTokenStarted,
} from './auth';
import {
    watchGetTutorias,
    watchAddTutorias,
    watchDeleteTutorias
} from './tutorias'

import {
  watchFetchConversations,
  watchAddConversation,
  watchRemoveConversation,
} from './conversations';

import {
  watchFetchMessages,
  watchAddMessage,
  watchRemoveMessage,
} from './messages';

import {
    watchRemoveFavTutor,
    watchAddFavTutor,
    watchFetchFavTutors,
} from './tutores';

import { watchSignUpTutoradoStarted,} from './signUpTutorado';
import {watchSignUpTutorStarted} from './signUpTutor';

import {
    watchRemoveFavTutor,
    watchAddFavTutor,
    fetchFavTutors,
} from './tutores';



function* mainSaga() {
  yield all([
    fork(watchLoginStarted),
    fork(watchRefreshTokenStarted),
    fork(watchGetTutorias),
    fork(watchAddTutorias),
    fork(watchDeleteTutorias),
    fork(watchFetchConversations),
    fork(watchAddConversation),
    fork(watchRemoveConversation),
    fork(watchFetchMessages),
    fork(watchAddMessage),
    fork(watchRemoveMessage),
    fork(watchRemoveFavTutor),       
    fork(watchAddFavTutor),
    fork(watchFetchFavTutors),
    fork(watchSignUpTutoradoStarted),
    fork(watchSignUpTutorStarted),
    fork(watchRemoveFavTutor),       
    fork(watchAddFavTutor),
    fork(fetchFavTutors)
  ]);
}


export default mainSaga;
