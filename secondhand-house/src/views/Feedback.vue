<template>
  <topNav></topNav>
  <span>用户反馈收集</span>
  <el-card class="card">
    <el-form
      :model="feedbacks"
      :rules="rules"
      class="demo-ruleForm"
      ref="feedbackForm"
    >
      <el-form-item label="展示效果评价" prop="uiScore">
        <el-rate
          v-model="feedbacks.uiScore"
          show-score
          text-color="#ff9900"
          score-template="{value} points"
        />
      </el-form-item>
      <el-form-item label="展示内容评价" prop="funScore">
        <el-rate
          v-model="feedbacks.funScore"
          show-score
          text-color="#ff9900"
          score-template="{value} points"
        />
      </el-form-item>
      <el-form-item label="总体效果评价" prop="totalScore">
        <el-rate
          v-model="feedbacks.totalScore"
          show-score
          text-color="#ff9900"
          score-template="{value} points"
        />
      </el-form-item>
      <el-form-item label="用户建议" prop="content">
        <el-input
          v-model="feedbacks.content"
          :rows="5"
          type="textarea"
          placeholder="请输入对本系统的建议，谢谢"
        />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submit(feedbackForm)"
          >提交反馈</el-button
        >
        <el-button @click="reset(feedbackForm)">重置</el-button>
      </el-form-item>
    </el-form>
  </el-card>
</template>
    
<script setup>
import { ElMessage } from "element-plus";
import { ref, reactive } from "vue";
import { feedback } from "../untils/request";
//定义表单实例
let feedbackForm = ref();
//定义存储用户反馈内容
let feedbacks = reactive({
  uiScore: 0,
  funScore: 0,
  totalScore: 0,
  content: "",
});
//定义表单校验规则
const rules = reactive({
  uiScore: [{ required: true, message: "请评价展示效果", trigger: "blur" }],
  funScore: [{ required: true, message: "请评价展示内容", trigger: "blur" }],
  totalScore: [{ required: true, message: "请评价总体效果", trigger: "blur" }],
  content: [{ required: true, message: "请输入用户建议", trigger: "blur" }],
});

//定义提交表单方法
const submit = (feedbackForm) => {
  feedbackForm.validate((valid) => {
    if (valid) {
      feedback(feedbacks).then((res) => {
        if (res.code == 200) {
          ElMessage.success(res.message);
          reset(feedbackForm);
        } else {
          ElMessage.error("提交失败");
        }
      });
      reset(feedbackForm);
    } else {
      console.log("提交失败");
    }
  });
};
//定义重置表单方法
const reset = (feedbackForm) => {
  feedbackForm.resetFields();
};
</script>
    
<style lang="scss" scoped>
span {
  font-size: 16px;
  position: absolute;
  left: 46%;
  top: 20%;
}
.card {
  width: 500px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
  margin-top: 10%;
}
</style>