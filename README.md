# aws-sam-practise

AWS Serverless Application Model(SAM) を使用したサンプルコードです。

## Files

- src - Lambda functionで使用されるコード.
- events - Invocation events that you can use to invoke the function.
- tests - Unit tests for the application code. 
- template.yaml - A template that defines the application's AWS resources.
- samconfig.toml - ```sam deploy``` 実行時に参照される設定ファイル.

## Deploy

```bash
sam build
sam deploy --guided  # --guidedオプションを使用するのは初回のみ.
```

## Use the SAM CLI to build and test locally

```bash
aws-sam-practise$ sam build --use-container
aws-sam-practise$ sam local start-api
aws-sam-practise$ curl http://localhost:3000/
```

Run functions locally and invoke them with the `sam local invoke` command.

```bash
aws-sam-practise$ sam local invoke HelloWorldFunction --event events/event.json
```

## Fetch, tail, and filter Lambda function logs

```bash
aws-sam-practise$ sam logs -n DefaultFunction --stack-name aws-sam-practise --tail
```

## Unit tests

```bash
aws-sam-practise$ python -m pytest tests/ -v
```

## Cleanup

```bash
aws cloudformation delete-stack --stack-name aws-sam-practise
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)

* [PyCharm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [IntelliJ](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html)
* [Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/welcome.html)
