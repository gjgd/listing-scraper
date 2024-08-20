import { Cron, Function } from "sst/constructs";

const Backend = ({ stack }) => {
  // const SLACK_TOKEN = new Config.Secret(stack, "SLACK_TOKEN");
  const isDev = stack.stage === 'dev';

  const cronFunction = new Function(stack, "function", {
    handler: "./cron/cron.main",
    runtime: "python3.11",
    timeout: 1 * 60,
    // bind: [SLACK_TOKEN],
  });

  const cron = new Cron(stack, "cron", {
    // schedule: "rate(1 minute)", // https://docs.sst.dev/cron-jobs
    schedule: "rate(5 minutes)", // https://docs.sst.dev/cron-jobs
    job: cronFunction,
    enabled: !isDev,
  });
};

export default {
  // eslint-disable-next-line no-unused-vars
  config(_input) {
    return {
      name: "stubhub-cron",
      region: "us-east-1",
      profile: "sst",
    };
  },
  stacks(app) {
    app.stack(Backend);
  },
};
