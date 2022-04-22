import {createAction, props} from '@ngrx/store';
import {FileModel} from '../../file/models/file.model';

export const upload = createAction('[Upload] Upload', props<{ file: FileModel }>());
export const uploadSuccess = createAction('[Upload] Upload Success', props<{ file: FileModel }>());
export const uploadFail = createAction('[Upload] Upload Fail', props<{ error: any }>());
export const uploadProgress = createAction('[Upload] Upload Progress', props<{ progress: number }>());
export const uploadCancel = createAction('[Upload] Upload Cancel', props<{ file: FileModel }>());
